import dash
from dash import dcc, html, Input, Output
import os
from chatbot import ChatbotSystem
from config import FILE, LLM

class OncologistAIApp:
    def __init__(self):
        """
        Initialize the OncologistAIApp class.

        This constructor sets up the Dash app, loads the chatbot model, and initializes the app layout.
        """
        # Define external CSS stylesheets from CDN
        self.external_stylesheets = [
            'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css',
            'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css',
        ]

        # Create the Dash app with external stylesheets
        self.app = dash.Dash(__name__, external_stylesheets=self.external_stylesheets)
        self.app.title = "OncologistAI"
        
        # Sample Questions
        self.sample_questions = [
            "What's the weather today?",
            "Tell me a joke.",
            "Who is the president of the United States?",
            "What's the capital of France?",
            "Can you recommend a good book?",
        ]
        
        # Create a list to store chat history
        self.chat_history = []

        # Load the chatbot model and initialize the app layout
        self.load_chatbot_model()
        self.initialize_layout()

    def load_chatbot_model(self):
        """
        Load the chatbot model.

        This function creates an instance of the ChatbotSystem class and loads the pre-trained language model.
        """
        self.chatbot_system = ChatbotSystem(
            file_path=FILE,
            llm_name=LLM,
            temperature=0,
            chunk_size=2000,
            chunk_overlap=200,
            k=4
        )
        self.chatbot_system.load_db()

    def initialize_layout(self):
        """
        Initialize the app layout.

        This function sets up the layout of the Dash app, including the HTML elements and CSS styling.
        """
        self.app.layout = html.Div(
            style={
                'backgroundImage': 'url("assets/cancer.jpeg")',
                'backgroundSize': 'cover',
                'backgroundRepeat': 'no-repeat',
                'minHeight': '100vh',
                'display': 'flex',
                'flexDirection': 'column',
                'alignItems': 'center',
                'justifyContent': 'flex-start',
            },
            children=[
                # Header section
                html.Div(
                    className='p-1 mb-2 bg-transparent text-white rounded-lg',
                    style={'textAlign': 'center', 'width': '90%', 'marginTop': '80px'},
                    children=[
                        html.H1("OncologistAI", className='display-4'),
                        html.P("Ask me anything related to Cancer Research!", className='lead'),
                    ]
                ),
                # Sample questions section
                html.Div(
                    className='p-2 mb-2 bg-transparent text-white rounded-lg',
                    style={'textAlign': 'center', 'width': '90%', 'maxWidth': '900px'},
                    children=[
                        html.P("Sample Questions:", style={'fontWeight': 'bold', 'fontSize': '18px'}),
                        html.Div([html.P(question, id=f'sample-question{i}', style={'margin': '5px'}) for i, question in enumerate(self.sample_questions)])
                    ]
                ),
                # Input box and send icon section
                html.Div(
                    id='input-container',
                    className='position-relative',
                    style={'textAlign': 'center', 'width': '90%', 'maxWidth': '900px'},
                    children=[
                        dcc.Input(
                            id='input-box',
                            type='text',
                            className='form-control',
                            placeholder='Enter your message...',
                            style={'paddingRight': '40px'},
                        ),
                        html.I(className='fa-solid fa-paper-plane', id='send-icon',
                               style={'position': 'absolute', 'top': '10px', 'right': '10px', 'fontSize': '20px', 'color': 'gray'}),
                    ]
                ),
                # Output container to display chat history
                html.Div(id='output-container', className='mt-3 p-3 bg-dark text-white rounded', style={'marginTop': '180px'}),
            ]
        )

        # Create the callbacks for the app
        self.create_callbacks()

    def create_callbacks(self):
        """
        Create the Dash app callbacks.

        This function defines the callbacks for updating the send icon visibility and generating responses.
        """
        # Callback to handle input value and update send icon visibility
        @self.app.callback(
            Output('send-icon', 'style'),
            [Input('input-box', 'value')]
        )
        def update_send_icon_visibility(input_value):
            return {'position': 'absolute', 'top': '10px', 'right': '10px', 'fontSize': '20px', 'color': 'gray',
                    'visibility': 'visible' if input_value else 'hidden'}

        # Callback to handle button click and provide responses
        @self.app.callback(
            [Output('output-container', 'children'),
             Output('input-box', 'value')],
            [Input('input-box', 'n_submit')],
            [dash.dependencies.State('input-box', 'value')]
        )
        def generate_response(n_submit, input_value):
            if n_submit is not None and input_value:
                user_message = html.Div([
                    html.Span("You Asked: ", className="font-weight-bold text-success"),
                    html.Span(f"{input_value}")
                ])

                answer = self.model_response(input_value)
                response = html.Div([
                    html.Span("OncologistAI: ", className="font-weight-bold text-primary"),
                    html.Span(f"{answer}")
                ])

                # Add the user message and AI response to the chat history with line breaks in between
                self.chat_history.append(user_message)
                self.chat_history.append(html.Br())
                self.chat_history.append(response)
                self.chat_history.append(html.Br())
                self.chat_history.append(html.Br())
                self.chat_history.append(html.Br())

                # Join chat history with line breaks to display each message on a new line
                chat_history_display = html.Div([msg for msg in self.chat_history + [html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br()]])
                return chat_history_display, ""
            elif n_submit is not None and not input_value:
                return "Please enter a message.", ''
            return dash.no_update, ''

    def model_response(self, user_question):
        """
        Get the AI model's response to the user's question.

        Parameters:
            user_question (str): The user's input question.

        Returns:
            str: The AI model's response to the user's question.
        """
        return self.chatbot_system.chat(user_question)

    def run_app(self):
        """
        Run the OncologistAIApp.

        This function starts the Dash app server in debug mode.
        """
        self.app.run_server(debug=True)


if __name__ == '__main__':
    app = OncologistAIApp()
    app.run_app()
