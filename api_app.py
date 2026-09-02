app = FastAPI(
    title="API de génération d'images à configuration fixe",
    version="1.0.0"  #1
)

class GenerateIn(BaseModel):
    input: str = Field(...,
description="Requête en langage naturel (l'agent formule le prompt)."
)  #2

@app.post("/generate", response_class=Response)  #3
async def generate(body: GenerateIn):
    agent = build_agent()
    with trace("Génération d'image"):
        result = await Runner.run(agent, body.input)

    b64 = extract_image_b64(result)  #4
    if not b64:
        raise HTTPException(
            status_code=500, detail="L'outil de génération d'images n'a produit aucune sortie."
        )

    png_bytes = base64.b64decode(b64)
    return Response(content=png_bytes, media_type="image/png")  #5

#1 Crée l'application qui hébergera l'API
#2 Crée une classe de données typée pour contraindre l'entrée de l'API
#3 Enveloppe un décorateur app.post autour de la fonction qui consomme la requête entrante
#4 Les images sont traitées comme des chaînes base64. Extrait l'image en une chaîne base64.
#5 Renvoie l'image sous forme d'un tableau d'octets, mais l'image base64 pourrait également être renvoyée

"""
Pour exécuter ce code :
uvicorn chapter08.02_app:app --host 0.0.0.0 --port 8000 --reload

Une fois l'API lancée, l'appeler avec cURL :
curl.exe -s -X POST "http://localhost:8000/generate" `
-H "Content-Type: application/json" `
--data '{"input":"an agent generating an image"}' `
--output "out.png"

Ou alors avec Powershell :
Invoke-WebRequest -Uri "http://localhost:8000/generate" `
-Method Post `
-Headers @{ "Content-Type" = "application/json"; "Accept" = "image/png" } `
-Body '{"input":"an agent generating an image"}' `
-OutFile "out.png"
"""
