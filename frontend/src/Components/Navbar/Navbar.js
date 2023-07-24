import { AppBar, Toolbar, Typography } from '@mui/material';
import { ReactComponent as LogoBlack } from '../../img/logoBlack.svg';
import { ReactComponent as LogoGray } from '../../img/logoGray.svg';
import { useNavigate, useLocation } from 'react-router-dom';

function Navbar() {

    const navigate = useNavigate()
    const location = useLocation()
    const isHome = location.pathname === "/"

    return (
        <AppBar position = "fixed" 
                sx={
                    { backgroundColor: 'transparent', 
                    boxShadow: 'none' }
                    }>
            <Toolbar sx={{ cursor:'pointer'}} onClick={()=>{navigate("/")}}>
                { isHome ? <LogoGray width={30} height={30} /> : <LogoBlack width={40} height={40} />  }
                <Typography variant="h4" 
                    sx={{ marginLeft: '0.2%', cursor:'pointer' }}
                    color = {isHome ? "#CCCAD7" : "#4E5E7E"}
                >
                    TravelBuddy
                </Typography>
            </Toolbar>
        </AppBar>
    )

}

export default Navbar