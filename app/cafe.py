from datetime import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor is not vaccined.")

        expiration_date = visitor["vaccine"].get("expiration_date")

        if not expiration_date:
            raise OutdatedVaccineError("Vaccine expiration date is missing.")

        if expiration_date < datetime.now().date():
            raise OutdatedVaccineError("Vaccine is expirited.")

        if not visitor.get("wear masks", False):
            raise NotWearingMaskError("Visitor is not wearing a mask.")

        return f"Welcome to {self.name}"
