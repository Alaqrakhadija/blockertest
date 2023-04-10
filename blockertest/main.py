import typer


app = typer.Typer()


@app.command()
def shoot():
    """
    Shoot the portal gun
    """
    typer.echo("Shooting portal gun")

@app.command()
def greet():

    typer.echo("greeting")




@app.command()
def greet():
    typer.echo("greeting")