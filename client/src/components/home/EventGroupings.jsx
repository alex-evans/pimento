import React from 'react'
import GroupingHeader from './GroupingHeader'
import EventPlayers from './EventPlayers'

class EventGroupings extends React.Component {

    constructor(props) {
        super(props)
    }

    render() {
        return (
            <div>
                <table className="table table-striped table-boardered">
                    <GroupingHeader />
                    <EventPlayers />
                </table>
            </div>
        )
    }
}

export default EventGroupings