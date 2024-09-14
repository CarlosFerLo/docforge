import typer

import os
from pathlib import Path

app = typer.Typer()

@app.command()
def new(name: str):
    """
    Create a new DocForge directory.
    """
    forge_path = Path(name)
    
    if forge_path.is_dir() :
        if (forge_path / "docforge.json").exists() :
            typer.secho(f"The forge '{name}' already exists!")
            raise typer.Exit(1)
        
        typer.secho(f"The directory '{name}' already exists.")
        
    else :
        typer.secho(f"Creating '{name}' forge...")
        forge_path.mkdir()

    typer.secho("Creating 'docforge.json' configuration file...")
    with open(forge_path / "docforge.json", "w") as f :
        f.write( "{\nname: \"" + name + "\"\n}")
        
    typer.secho("Forge successfully initialized!")
