# Deforum Stable Diffusion Chatbot
Understanding or locating the correct configuration for deforum stable diffusion can be puzzling. As a solution, I opted to organize its documentation for easy searching. This application is a chatbot powered by OpenAI GPT and utilizes deforum stable diffusion to assist developers in effectively searching through documentations.

Feel free to to contribute to and expand its documentation.

Deforum Stable Diffusion is a version of Stable Diffusion focussing on creating videos and transitions of images created with Stable Diffusion. By employing Deforum Stable Diffusion, you can produce captivating videos similar to the example provided below.



https://github.com/ElmiraGhorbani/deforum_stable_diffusion_chatbot/assets/23237541/87ba1b98-0044-438f-8bd6-522d205921d4




## Getting started

NOTE: set your OpenAI API key.  (source in ./scripts/app.py and .env.example)
```
cp .env.example .env

```

```

docker-compose up -d

```

## Testing
open FastApi swagger, hit try it out.

![teaser](./resource/images/request.png)

```
http://0.0.0.0:8086/docs
```

![teaser](./resource/images/response.png)
