import React from 'react'
import Event from './home/Event'
import Header from './home/Header'

class App extends React.Component {
  render() {
    return (
      <div>
        <Header />
        <Event />
      </div>
    )
  }
}

export default App