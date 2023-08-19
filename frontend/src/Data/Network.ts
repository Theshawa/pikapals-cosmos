import {API_BASE_URL} from '../env.ts'

class Network {
    apiBaseURL: string

    constructor(apiBaseURL: string) {
        this.apiBaseURL = apiBaseURL
    }

    private sendHttpRequest = (method: string, url: string, data: object = {}): Promise<any> => {
        return new Promise((resolve, reject) => {
            const xhr = new XMLHttpRequest()
            xhr.withCredentials = true
            xhr.open(method, this.apiBaseURL + url)
            xhr.responseType = 'json'

            if (data && Object.keys(data).length !== 0) {
                xhr.setRequestHeader('Content-Type', 'application/json')
            }

            xhr.onload = async () => {
                if (xhr.status >= 400) {
                    let errorMessage: string | null = null
                    if (xhr.response != null && Object.prototype.hasOwnProperty.call(xhr.response, 'data') && Object.prototype.hasOwnProperty.call(xhr.response, 'error')) {
                        errorMessage = xhr.response.data.error
                    }
                    reject(new NetworkError(xhr.status, url, xhr.response?.message, errorMessage ?? ''))
                } else {
                    resolve(xhr.response.data)
                }
            }

            xhr.onerror = () => {
                reject('Network Failure')
            }
        })
    }
}

export class NetworkError {
    statusCode: number
    url: string
    message?: string
    errorDescription?: string
    stack?: string;

    constructor(statusCode: number, url: string, message?: string, description?: string) {
        this.statusCode = statusCode
        this.url = url
        this.message = message
        this.errorDescription = description
        this.stack = new Error().stack
    }
}

const NETWORK = new Network(API_BASE_URL)
export default NETWORK