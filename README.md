# Using sqlalchemy in 2025

So another year passes and things get cleverer and scarier

We need to understand how to use dataclasses and type hinting to help the magic

I needed to tweak my use of relationship to use sqlalchemy.orm.Mapped, which was pretty much ok but
- we them need to declare default values (when a kwarg isn't provided)
- this therefore means providing a default_factory

I also needed to remember that classes can be referred to before their definition as long as they are enclosed in quotes

More anon...

