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

export default EmbeddedContent;
