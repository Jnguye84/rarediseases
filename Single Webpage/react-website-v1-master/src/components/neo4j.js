import React from 'react';
import './neo4j.css';


function EmbeddedContent() {
  return (
    <div>
      {/* Replace the src attribute with your external URL */}
      <iframe
        src="http://localhost:7474/browser/"
        width="540"
        height="450"
        title="Embedded Content"
      />
    </div>
  );
}


function Neo4j() {
  return (
    <div>
    <br></br>
    <h1 className="heading">(Insert Neo4J)</h1>
    <button class="primary-button">Add Nodes</button>
  <button class="secondary-button">Remove Nodes</button>
  <button class="success-button">Nearest Specialized Caretaker</button>
    {/* <div className='neo4j-btns'>
        <Button
          className='btns'
          buttonStyle='btn--outline'
          buttonSize='btn--large'
        >
          GET STARTED
        </Button>
        <Button
          className='btns'
          buttonStyle='btn--primary'
          buttonSize='btn--large'
          onClick={console.log('hey')}
        >
          WATCH TRAILER <i className='far fa-play-circle' />
        </Button>
      </div> */}
    </div>
  );
}

export default Neo4j;
