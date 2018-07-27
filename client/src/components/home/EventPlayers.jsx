import React from 'react'
import axios from 'axios'

class EventPlayers extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            event_players: []
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:5000/event')
            .then(json => console.log(json))
    }

    render() {
        return (
            <div>
                <tbody>
                    <tr>
                        <th scope="row">test</th>
                    </tr>
                </tbody>
            </div>
        )
    }
}

export default EventPlayers