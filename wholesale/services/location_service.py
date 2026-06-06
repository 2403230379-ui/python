from fastapi import HTTPException
from starlette import status
from datetime import datetime, timezone

from dtos.location.location_response import LocationResponseDTO
from dtos.location.location_create import LocationCreateDTO
from dtos.location.location_update import LocationUpdateDTO

from services.client_service import ClientService

from simulations.locations_data import locations_data
locations = locations_data

class LocationService:

    @staticmethod
    def get_locations():
        active_locations = []
        for location in locations:
            if location.active == True:
                active_locations.append(location)
        return active_locations

    @staticmethod
    def find_location(location_id: int):
        found_location = None
        for location in locations:
            if location.id == location_id:
                found_location = location

        if found_location is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Location not found"
            )

        return found_location

    @staticmethod
    def create_location(dto: LocationCreateDTO):
        new_id = len(locations) + 1

        ClientService.find_client(client_id=dto.client_id)

        now = datetime.now(timezone.utc)

        new_location = LocationResponseDTO(
            id=new_id,
            client_id=dto.client_id,
            name=dto.name,
            address=dto.address,
            city=dto.city,
            state=dto.state,
            postal_code=dto.postal_code,
            phone=dto.phone,
            email=dto.email,
            active=True,
            created_at=now,
            updated_at=now
        )

        locations.append(new_location)

        return new_location

    @staticmethod
    def update_location(dto: LocationUpdateDTO):
        location = LocationService.find_location(location_id=dto.id)

        ClientService.find_client(client_id=dto.client_id)

        location.client_id = dto.client_id
        location.name = dto.name
        location.address = dto.address
        location.city = dto.city
        location.state = dto.state
        location.postal_code = dto.postal_code
        location.phone = dto.phone
        location.email = dto.email
        location.updated_at = datetime.now(timezone.utc)

        return location

    @staticmethod
    def delete_location(location_id: int):
        location = LocationService.find_location(location_id=location_id)

        location.active = False
        location.updated_at = datetime.now(timezone.utc)

        return location
