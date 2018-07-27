import React from 'react'
import axios from 'axios'
import EventGroupings from './EventGroupings'

class Event extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            groupA: [],
            groupB: [],
            groupC: [],
            groupD: []
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:5000/event')
            .then(json => json.data)
            .then(newData => this.setState(
                {
                    groupA: newData["A"],
                    groupB: newData["B"],
                    groupC: newData["C"],
                    groupD: newData["D"]
                }))
            .catch(error => alert(error))
    }

    render() {
        return (
            <div>
                <EventGroupings />
                {this.state.groupA}
                {this.state.groupB}
                {this.state.groupC}
                {this.state.groupD}
            </div>
        )
    }
}

export default Event