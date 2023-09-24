import os
import openai
import time

openai.api_key = input("Enter your OpenAI key: ") 

# Define the folder structure (an example from my Github) 
folder_structure = {
    "Machine Learning": {
        "Unsupervised Learning": {
            "Clustering": {
                "Hierarchical Clustering": []
            },
            "Dimensionality Reduction": {
                "Principal Component Analysis (PCA)": ["SOP Dataset"],
                "t-Distributed Stochastic Neighbour Embedding (t-SNE)": [],
                "Linear Discriminant Analysis (LDA)": []
            },
            "Association Rule Learning": []
        },
        "Reinforcement Learning": [],
        "Model Evaluation and Validation": {
            "Cross-validation": [],
            "Hyperparameter Tuning": [],
            "Model Selection Techniques": [],
            "Evaluation Metrics": [],
            "Advanced Machine Learning": {
                "Ensemble Methods (Bagging, Boosting)": [],
                "Learning Curves and Bias-Variance Tradeoff": [],
                "Model Interpretability and Explainability (SHAP, LIME)": []
            }
        }
    },
    "Deep Learning": {
        "Neural Networks": {
            "Perceptron": [],
            "Multi-Layer Perceptron (MLP)": []
        },
        "Convolutional Neural Networks (CNNs)": {
            "Image Classification": [],
            "Object Detection": [],
            "Image Segmentation": []
        },
        "Recurrent Neural Networks (RNNs)": {
            "Sequence-to-Sequence Models": [],
            "Text Classification": [],
            "Sentiment Analysis": []
        },
        "Long Short-Term Memory (LSTM) and Gated Recurrent Units (GRU)": {
            "Time Series Forecasting": [],
            "Language Modelling": []
        },
        "Generative Adversarial Networks (GANs)": {
            "Image Synthesis": [],
            "Style Transfer": [],
            "Data Augmentation": []
        },
        "Advanced Deep Learning": {
            "Attention Mechanisms": [],
            "Transfer Learning": [],
            "Self-Supervised Learning": []
        }
    },
    "Advanced Topics": {
        "Natural Language Processing (NLP)": {
            "Text Preprocessing": [],
            "Word Embeddings (e.g., Word2Vec, GloVe)": [],
            "Recurrent Neural Networks for NLP": [],
            "Transformer Models (e.g., BERT, GPT)": []
        },
        "Time Series Analysis": {
            "Time Series Decomposition": [],
            "Autoregressive Integrated Moving Average (ARIMA)": [],
            "Seasonal ARIMA (SARIMA)": [],
            "Exponential Smoothing Methods": [],
            "Prophet": []
        },
        "Recommender Systems": {
            "Collaborative Filtering": [],
            "Content-Based Filtering": [],
            "Matrix Factorization": [],
            "Hybrid Methods": []
        },
        "Causal Inference": {
            "Experimental Design": [],
            "Observational Studies": [],
            "Propensity Score Matching": [],
            "Instrumental Variable Analysis": []
        },
        "Advanced Deep Learning": {
            "Advanced Architectures (e.g., Transformers, GPT models)": [],
            "Generative Models (e.g., VAEs, flow-based models)": [],
            "Advanced Techniques for NLP and Computer Vision": []
        },
        "Bayesian Statistics and Probabilistic Programming": {
            "Bayesian Inference": [],
            "Markov Chain Monte Carlo (MCMC)": [],
            "Probabilistic Graphical Models": [],
            "Stan, PyMC3, or Edward for Probabilistic Programming": []
        },
        "Automated Machine Learning (AutoML)": [],
        "Data Engineering": {
            "ETL (Extract, Transform, Load) processes": [],
            "Data Warehousing": []
        }
    },
    "Big Data Technologies": {
        "Hadoop": [],
        "HDFS": [],
        "MapReduce": [],
        "Spark": {
            "RDDs": [],
            "DataFrames": [],
            "MLlib": []
        },
        "NoSQL Databases": {
            "MongoDB": [],
            "Cassandra": [],
            "HBase": [],
            "Couchbase": []
        },
        "Stream Processing Frameworks": {
            "Apache Kafka": [],
            "Apache Flink": [],
            "Apache Storm": []
        }
    },
    "Algorithms": {
        "Hill Climb": [],
        "Genetic Algorithm": [],
        "Beam Search": []
    },
    "Data Visualisation and Reporting": {
        "Dashboarding Tools": {
            "Tableau": [],
            "PowerBI": [],
            "Dash (Python)": [],
            "Shiny (R)": []
        },
        "Storytelling with Data": [],
        "Effective Communication": []
    },
    "Domain Knowledge and Soft Skills": {
        "Industry-specific Knowledge": [],
        "Problem-solving": [],
        "Communication Skills": [],
        "Time Management": [],
        "Teamwork": [],
        "Business Acumen": {
            "Understanding of business metrics and Key Performance Indicators (KPIs)": [],
            "Ability to translate business problems into data problems and vice versa": []
        }
    },
    "Ethical Considerations and Bias in Data Science": {
        "Fairness in Machine Learning": [],
        "Bias Detection and Mitigation": [],
        "Privacy and Data Security": [],
        "Zook's 5 A": [],
        "Data Privacy and Governance": {
            "Understanding regulations like GDPR, CCPA": [],
            "Data anonymisation and pseudonymisation techniques": []
        }
    },
    "Deployment and Productionisation": {
        "Model Deployment Techniques": [],
        "Containerisation (Docker, Kubernetes)": [],
        "Microservices": [],
        "Serverless Computing": [],
        "Cloud Platforms": {
            "AWS": [],
            "Azure": [],
            "GCP": [],
            "IBM Cloud": []
        }
    }
}

        def gpt_fill_md(topic):
            completion = openai.ChatCompletion.create(
              model="gpt-4", 
              messages=[{"role": "user", "content": f"Generate me a full markdown document covering {topic} for my GitHub notebook. Write `Created by @jl33-ai 👦🏻` under the title. Use dotpoints, tags, emojis and examples, and be very clear and concise."}]
            )
            
            md_content = completion['choices'][0]['message']['content']
            return md_content

def create_directory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

def create_md_file(file_name, tags=[]):
    with open(f"{file_name}.md", 'w') as file:
        # file.write("# " + file_name.replace("-", " ").title() + "\n")
        # Call your 'gpt_fill' function here
        start_time = time.time()
        content = gpt_fill_md(file_name)

        lines = content.strip().split('\n')  # Split the string into lines and remove leading/trailing whitespaces
        content_without_first_and_last = '\n'.join(lines[1:-1])  # Exclude the first and last lines
        file.write(content_without_first_and_last)
        end_time = time.time()
        print(f"📄 Successfully created {file_name}.md | Took {round(end_time-start_time, 1)} seconds")

def sanitize_topic_name(topic):
    return str(topic).lower().replace(" ", "-").replace("(","").replace(")","")

def recursive_file(parent):
    """Uses recursion to traverse nested dictionairy.
Procedural automation of an entire wikipedia.
Create list -> Parse list -> Generate full Markdown w/ openAI API"""
    

    for topic in parent:
        if isinstance(parent[topic], list):
            file_name = sanitize_topic_name(topic)
            create_md_file(file_name)
        else:
            recursive_file(parent[topic])

recursive_file(folder_structure)
# create_md_file('bayesian-statistics')
