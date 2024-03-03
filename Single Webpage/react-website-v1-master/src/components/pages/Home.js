import React from 'react';
import '../../App.css';
import Neo4j from '../neo4j';
import EmbeddedContent from '../neoframe';
import HeroSection from '../HeroSection';

function Home() {
  return (
    <>
      <HeroSection />
      <Neo4j />
      <EmbeddedContent />
    </>
  );
}

export default Home;
