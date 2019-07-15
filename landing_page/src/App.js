import React from "react";
import styled from "styled-components";

import MainContainer from "./components/Container";
import SearchBar from "./components/SearchBar";
import SearchButtons from "./components/Buttons";

import HeaderImage from "./images/redscout.png";

const HeaderImg = styled.img`
  width: 30vw;
  padding-bottom: 2.5vh;
`;

const Tagline = styled.div`
  position: absolute;
  transform: translateY(45vh);
  font-size: 1rem;
  color: #444242;
  padding-bottom: 2.5vh;
  font-weight: 600;
  user-select: none;
`;

function App() {
  return (
    <div className="App">
      <MainContainer>
        <div
          style={{
            width: "50vw",
            textAlign: "center",
            transform: "translateY(-5vh)"
          }}
        >
          <HeaderImg src={HeaderImage} />
          <SearchBar />
          <SearchButtons />
        </div>
        <Tagline>
          * Completely uncensored search, brought to you by the KGB. &copy;
          Putin 2019.
        </Tagline>
      </MainContainer>
    </div>
  );
}

export default App;
