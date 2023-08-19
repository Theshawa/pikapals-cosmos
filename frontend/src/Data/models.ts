export class Seat {
    id: string
    voyage: string
    seat_no: number
    price: number
    available: boolean
    seatClass: SeatClass
    bookedBy: string

    constructor(id: string, voyage: string, seat_no: number, price: number, available: boolean, seat_class: string, booked_by: string) {
        this.id = id
        this.voyage = voyage
        this.seat_no = seat_no
        this.price = price
        this.available = available
        this.seatClass = SeatClass[seat_class as keyof typeof SeatClass]
        this.bookedBy = booked_by
    }
}

export enum SeatClass {
    ECONOMY = "ECONOMY",
    BUSINESS = "BUSINESS",
    FIRST = "FIRST"
}

export class Voyage {
    voyage_no: string
    start: string
    destination: string
    departure_time: string
    arrival_time: string
    min_ticket_price: number
    service_provider: string

    constructor(voyage_no: string, start: string, destination: string, departure_time: string, arrival_time: string, min_ticket_price: number, service_provider: string) {
        this.voyage_no = voyage_no
        this.start = start
        this.destination = destination
        this.departure_time = departure_time
        this.arrival_time = arrival_time
        this.min_ticket_price = min_ticket_price
        this.service_provider = service_provider
    }
}

export class ServiceProvider {
    id: string
    name: string

    constructor(id: string, name: string) {
        this.id = id
        this.name = name
    }
}

export class Port {
    id: string
    name: string

    constructor(id: string, name: string) {
        this.id = id
        this.name = name
    }
}