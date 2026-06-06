from fastapi import HTTPException
from starlette import status
from datetime import datetime, timezone

from dtos.client.client_response import ClientResponseDTO
from dtos.client.client_create import ClientCreateDTO
from dtos.client.client_update import ClientUpdateDTO

from simulations.clients_data import clients_data
clients = clients_data

class ClientService:

    @staticmethod
    def get_clients():
        active_clients = []
        for client in clients:
            if client.active == True:
                active_clients.append(client)
        return active_clients

    @staticmethod
    def find_client(client_id: int):
        found_client = None
        for client in clients:
            if client.id == client_id:
                found_client = client

        if found_client is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Client not found"
            )

        return found_client

    @staticmethod
    def create_client(dto: ClientCreateDTO):
        new_id = len(clients) + 1

        now = datetime.now(timezone.utc)

        new_client = ClientResponseDTO(
            id=new_id,
            name=dto.name,
            phone=dto.phone,
            email=dto.email,
            rfc=dto.rfc,
            active=True,
            created_at=now,
            updated_at=now
        )

        clients.append(new_client)

        return new_client

    @staticmethod
    def update_client(dto: ClientUpdateDTO):
        client = ClientService.find_client(client_id=dto.id)

        client.name = dto.name
        client.phone = dto.phone
        client.email = dto.email
        client.rfc = dto.rfc
        client.updated_at = datetime.now(timezone.utc)

        return client

    @staticmethod
    def delete_client(client_id: int):
        client = ClientService.find_client(client_id=client_id)

        client.active = False
        client.updated_at = datetime.now(timezone.utc)

        return client
