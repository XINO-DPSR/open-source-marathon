import React from "react";
import styled from "styled-components";

const MainContainer = styled.div`
  height: 100vh;
  width: 100vw;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
`;

export default function Container(props) {
  return <MainContainer>{props.children}</MainContainer>;
}
