# Architecture Diagram (Textual)

Client (Next.js) -> API Gateway (FastAPI) -> PostgreSQL/Redis/Elasticsearch
                                     -> ML Engine services
                                     -> Payment providers (Stripe/PayPal)
                                     -> S3 object storage

The system is containerized with Docker Compose and deployable to AWS/Vercel.
