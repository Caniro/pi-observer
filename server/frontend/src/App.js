import React, { useState, useEffect } from "react";
import axios from 'axios';
import styled from 'styled-components';

const VideoWrapper = styled.a`
  color: black;
  display: block;
  margin: 1rem;
  text-decoration: none;
  &:hover {
  color: gray;
  }
`;

const App = () => {
  const [list, setList] = useState([]);
  useEffect(() => {
    axios.get('/list').then(response => {
      setList(response.data);
    });
  }, []);

  return (
    <div>
      {list.map(file => (
        <VideoWrapper href={'/file/' + file}>{file}</VideoWrapper>
      ))}
    </div>
  );
}

export default App;
