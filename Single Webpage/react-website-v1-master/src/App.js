import React from 'react';
import Navbar from './components/Navbar';
import './App.css';
import Home from './components/pages/Home';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import ContactInfo from './components/pages/ContactInfo';
import About from './components/pages/About';

function App() {
  return (
    <>
      <Router>
        <Navbar />
        <Switch>
          <Route path='/' exact component={Home} />
          <Route path='/contact-info' component={ContactInfo} />
          <Route path='/about' component={About} />
          
        </Switch>
      </Router>
    </>
  );
}

export default App;
