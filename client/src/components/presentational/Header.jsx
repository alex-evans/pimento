import React from 'react'

export default class Header extends React.Component {
  render() {
    return (
        <div>
            <nav className="navbar navbar-expand-lg navbar-light bg-light">
                <a className="navbar-brand" href="#">Pimento</a>
            </nav>
        </div>
    )
  }
}