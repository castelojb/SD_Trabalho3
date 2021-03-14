import styled from "styled-components";

export const Button = styled.button`
  background: transparent;
  border-radius: 10px;
  border: 2px solid blue;
  color: blue;
  padding: 10px;
  cursor: pointer;
`;

export const Container = styled.div`
  display: flex;
  @media (max-width: 800px) {
    flex-direction: column;
    position: relative;
  }
`;
