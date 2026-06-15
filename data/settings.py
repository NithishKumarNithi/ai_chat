settings = {
    "providers": ["openai", "gemini", "anthropic"],
    "selected": "",
    "models": [
        {
            "provider": "openai",
            "models": ["gpt-4", "gpt-5"]
        },
        {
            "provider": "gemini",
            "models": ["gemini-flash", "gemini-flash-2.5"]
        },
        {
            "provider": "anthropic",
            "models": ["opus", "sonnet"]
        }
    ]
}

user_settings= [
    {
        "user_id": 1,
        "settings" : {
            "provider" : "openai",
            "models" : "gpt-5"
        }
    },
    {
        "user_id": 5,
        "settings" : {
            "provider" : "anthropic",
            "models" : "opus"
        }
    },
    {
        "user_id": 3,
        "settings" : {
            "provider" : "gemini",
            "models" : "gemini-flast-2.5"
        }
    },
]