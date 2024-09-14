from pathlib import Path

from typer.testing import CliRunner

from docforge.cli.main import app


runner = CliRunner()
temp_dir = Path("tmp")

def test_new_command_with_standard_input() :
    with runner.isolated_filesystem() :
        result = runner.invoke(app, ["test-forge"])
        
        assert result.exit_code == 0
        
        assert "Creating 'test-forge' forge..." in result.stdout
        assert Path("test-forge").is_dir()
        
        assert "Creating 'docforge.json' configuration file..." in result.stdout
        assert Path("test-forge/docforge.json").exists()
        
        with open("test-forge/docforge.json", "r") as f:
            assert '{\nname: "test-forge"\n}' in f.read()  
            
        assert "Forge successfully initialized!" in result.stdout

def test_new_command_when_input_name_dir_already_exists () :
    with runner.isolated_filesystem() :
        Path("test-forge").mkdir()
        
        result = runner.invoke(app, ["test-forge"])
        
        assert result.exit_code == 0
        assert "The directory 'test-forge' already exists." in result.stdout
        
        assert "Creating 'docforge.json' configuration file..." in result.stdout
        assert Path("test-forge/docforge.json").exists()
        
        with open("test-forge/docforge.json", "r") as f:
            assert '{\nname: "test-forge"\n}' in f.read()  
            
        assert "Forge successfully initialized!" in result.stdout
        
def test_new_command_when_input_name_is_already_a_forge () :
    with runner.isolated_filesystem() :
        
        runner.invoke(app, ["test-forge"])
        result = runner.invoke(app, ["test-forge"])
        
        assert result.exit_code == 1
        assert "The forge 'test-forge' already exists!" in result.stdout

        