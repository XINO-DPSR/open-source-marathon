import React from "react";
import styled from "styled-components";

const Bar = styled.input`
  width: 49.5vw;
  height: 1.5rem;
  padding: 10px;
  margin: 0;
  font-size: 1.1em;
  border: 1px solid rgba(0, 0, 0, 0.15);
  border-radius: 8px;
  box-shadow: 0 2px 3px rgba(0, 0, 0, 0.06);
  display: block;
  &:focus {
    outline: none !important;
  }
`;

export default function SearchBar() {
  return <Bar />;
}
