import React from 'react'
import EventGroupings from './EventGroupings'
import Header from './presentational/Header'

export default class App extends React.Component {
  render() {
    return (
      <div>
        <Header />
        <EventGroupings />
      </div>
    )
  }
}