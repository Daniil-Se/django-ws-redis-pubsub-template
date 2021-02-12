let domenName = window.location.hostname

let config = {
	API_PATH: domenName === 'localhost' ? (
        'ws://localhost:8000/ws/params/'   // dev
    ) : (
        `wss://${domenName}/ws/params/` // prod
    )
}


class WebSocketService {

    static instance = null
    component_callback = null

    static getInstance() {
        if (!WebSocketService.instance) {
            WebSocketService.instance = new WebSocketService()
        }
        return WebSocketService.instance
    }

    constructor() {
        this.socketRef = null
    }

    connect() {
        const path = config.API_PATH
        this.socketRef = new WebSocket(path)

        this.socketRef.onopen = () => {
            console.log('WebSocket open')
        }
    	this.socketRef.onmessage = e => {
            console.log(e.data)
        	//this.socketNewMessage(e.data)
    	}
        this.socketRef.onerror = e => {
            console.log(e.message)
        }
        this.socketRef.onclose = () => {
            console.log("WebSocket closed let's reopen")
            this.connect()
        }
    }

    socketNewMessage(data) {
    	const parsedData = JSON.parse(data)
    	this.component_callback(parsedData)
    }

    addCallback(newMessageCallback) {
    	this.component_callback = newMessageCallback
    }
  
  	state() {
    	return this.socketRef.readyState;
  	}
}

const WebSocketInstance = WebSocketService.getInstance()
WebSocketInstance.connect()


export default WebSocketInstance
