from invoke import Context, task


@task
def generate(c: Context, slug):
    """Scaffold a new drop variant inside xo-drops."""
    c.run(f"python xo-drops/scripts/drop_generate.py {slug}")
