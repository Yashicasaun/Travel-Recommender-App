import React from 'react';
import { Typography } from '@mui/material';

const Apptext = () => {
  return (
    <div className='mainPage-text'
    style={{ 
        position: 'fixed', 
        bottom: '30%', 
        left: '10%', 
        width: '35%' }}>
    <Typography variant="body1" style={{
        fontFamily: 'system-ui', 
        fontSize: '2.2vh',
        color: "#EDEDED" }}>
        Embark on a hassle-free journey with us!
        <br/>
        Just pick your dream destination and let us know your preferences. 
        Our ingenious algorithms will craft multiple personalized routes tailored to your desires!
        <br/><br/>
        Let the adventure begin!
    </Typography>
    </div>
  );
};

export default Apptext;
