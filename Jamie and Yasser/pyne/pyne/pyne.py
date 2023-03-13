"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    xpoints:list = np.array([1, 8])
    ypoints:list = np.array([3, 10])

    
    
    """The app state."""
    @pc.var
    def plot(self):
        return px.scatter(
                [1,2,34,4,453], 
                x="Age", 
                y="Salary", 
                title="Age/Salary Distribution"
            )

        


    


def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading("Welcome to Pynecone!", font_size="2em"),
            pc.plotly(data=State.plot, layout={"width": "1000", "height": "600"}),
            pc.box("Get started by editing ", pc.code(filename, font_size="1em")),
            pc.link(
                "Check out our docs!",
                href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": "rgb(107,99,246)",
                },
            ),
            spacing="1.5em",
            font_size="2em",
        ),
        padding_top="10%",
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()
