import NETWORK from "./Network"
import {Port, Seat, ServiceProvider, Voyage} from "./models.ts";

export abstract class CacheObject<T> {
    protected data!: T | null
    protected lastUsed: number
    protected lastUpdated: number

    protected constructor() {
        this.lastUsed = 0
        this.lastUpdated = 0
    }

    abstract load(): Promise<T>

    async get(isRefresh = false): Promise<T> {
        if (this.data == null || isRefresh) {
            this.data = await this.load()
            this.lastUpdated = (new Date()).getTime()
        }

        this.lastUsed = new Date().getTime()

        return this.data
    }

    set(data: T) {
        this.data = data
        this.lastUpdated = (new Date()).getTime()
    }

    invalidateCache(): void {
        this.data = null
    }
}

export class SeatCache extends CacheObject<Seat> {
    constructor() {
        super()
    }

    async load(): Promise<Seat> {
        throw new Error("No endpoint. Cache has to be manually set.")
    }
}

export class PortCache extends CacheObject<Port> {
    constructor() {
        super()
    }

    async load(): Promise<Port> {
        throw new Error("No endpoint. Cache has to be manually set.")
    }
}

export class ServiceProviderCache extends CacheObject<ServiceProvider> {
    constructor() {
        super()
    }

    async load(): Promise<ServiceProvider> {
        throw new Error("No endpoint. Cache has to be manually set.")
    }
}

class Cache {
    private seatCache: { [seatId: string]: SeatCache }
    private portCache: { [portId: string]: PortCache }

    constructor() {
        this.seatCache = {}
    }

    getSeat(seatId: string) {
        if (this.seatCache[seatId] == null) {
            this.seatCache[seatId] = new SeatCache()
        }

        return this.seatCache[seatId]
    }

    getPort(portId: string) {
        if (this.portCache[portId] == null) {
            this.portCache[portId] = new PortCache()
        }

        return this.portCache[portId]
    }

    getServiceProvider(serviceProviderId: string) {
        if (this.portCache[serviceProviderId] == null) {
            this.portCache[serviceProviderId] = new ServiceProviderCache()
        }

        return this.portCache[serviceProviderId]
    }

    invalidateCache() {
        this.seatCache = {}
    }
}

const CACHE = new Cache()

export default CACHE