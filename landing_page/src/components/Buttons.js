import React from "react";
import styled from "styled-components";

const Search = styled.div`
  height: 3.8rem;
  width: 30%;
  background-color: #dc1d06;
  color: #fff;
  font-weight: 700;
  margin-right: 10px;
  border-radius: 5px;
  transition: all 0.3s ease-in-out;
  display: inline-flex;
  justify-content: center;
  align-items: center;
  user-select: none;
  cursor: pointer;
  &:hover {
    transform: translateY(-1px);
    box-shadow: 0 2px 3px rgba(0, 0, 0, 0.06);
  }
`;

const FeelingUnlucky = styled.div`
  height: 3.8rem;
  width: 30%;
  background-color: #d3d3d3;
  color: #444242;
  display: inline-block;
  margin-right: 10px;
  font-weight: 700;
  border-radius: 5px;
  display: inline-flex;
  justify-content: center;
  align-items: center;
  transition: all 0.3s ease-in-out;
  text-align: center;
  user-select: none;
  cursor: pointer;
  &:hover {
    transform: translateY(-1px);
    box-shadow: 0 2px 3px rgba(0, 0, 0, 0.06);
  }
`;

export default function SearchButtons(props) {
  return (
    <div style={{ display: "block", paddingTop: "5vh" }}>
      <Search onClick={() => alert("REDACTED REDACTED REDACTED")}>
        search comrade
      </Search>
      <FeelingUnlucky
        onClick={() =>
          window.open("https://www.youtube.com/watch?v=s9APLXM9Ei8", "_blank")
        }
      >
        i'm feeling unlucky
      </FeelingUnlucky>
    </div>
  );
}
