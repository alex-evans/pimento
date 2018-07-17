import React from 'react'

class Event extends React.Component {

    constructor(props) {
        super(props)
    }

    render() {
        return (
            <div>
                <thead className="thead-light">
                    <tr>
                        <th scope="col">Group A</th>
                        <th scope="col">Group B</th>
                        <th scope="col">Group C</th>
                        <th scope="col">Group D</th>
                    </tr>
                </thead>
            </div>
        )
    }
}

export default Event