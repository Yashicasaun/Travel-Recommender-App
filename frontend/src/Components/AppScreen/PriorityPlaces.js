import { useEffect, useState } from "react";
import styles from "./InterestsScreen.module.css"
import { Grid, Typography, Paper, TextField, Autocomplete, List, 
    ListItem, ListItemText, ListItemSecondaryAction, IconButton, Button } from "@mui/material"
import DeleteIcon from '@mui/icons-material/Delete';
import fetchPois from "../../api/endpoints/pois";
import { useLocation, useNavigate } from "react-router-dom";

function PriorityPlaces() {

    const [compulsoryPois, setCompulsoryPois] = useState([]);
    const [pois, setPois] = useState([])
    const location = useLocation()
    const navigate = useNavigate()

    const queryParams = new URLSearchParams(location.search);
    const categories = queryParams.get('categories')
    const city = queryParams.get('city')
      
    const handleItemSelected = (event, value) => {
        if (value) {
            setCompulsoryPois([...compulsoryPois, value]);
            const index = pois.indexOf(value)
            setPois((prevPois) => {
                prevPois.splice(index,1) 
                console.log(prevPois)
                return prevPois})
            }
      };
      
      const handleDelete = (index) => {
        setCompulsoryPois((prevSelectedItems) => prevSelectedItems.filter((_, i) => i !== index));
        setPois((prevSelectedItems) =>[...prevSelectedItems, compulsoryPois[index]])
      };

      const handleOnClick = () => {
        const queryParams = new URLSearchParams(location.search);
        queryParams.append('compulsory_pois', compulsoryPois)
        navigate(`/routes?${queryParams.toString()}`)
      }

      useEffect(() => {
        fetchPois(city, categories).then(
        (data => setPois(data))
        )
      }, [city, categories])

    return (
        <div className={styles.InterestsScreen}>
            <Grid
                container
                position="fixed"
                top="20%"
                left="20%"
                width="60%"
                height="70%"
                display="flex"
                justifyContent="left"
                alignItems="left"
                flexDirection="column"
                textAlign="left"
                >
                <Paper
                    elevation={3}
                    sx={{
                    p: 2,
                    maxHeight: '80%',
                    overflow: 'hidden',
                    background: 'transparent',
                    }}
                >
                    <Typography variant="h5" gutterBottom style={{ marginBottom: '1rem' }}>
                    Choose your must-visit destinations
                    </Typography>

                    <Autocomplete
                            options={pois}
                            onChange={handleItemSelected}
                            renderInput={(params) => <TextField {...params} label="Search" variant="outlined" />}
                            renderOption={(props, option) => (
                            <li {...props}>
                                <Typography variant="h7" >{option}</Typography>
                            </li>
                            )}
                            style={{ width: '100%' }}
                            clearOnEscape 
                    />
                    <div style={{ overflowY: 'scroll', height: 'calc(100% - 100px)' }}>
                        <List style={{ marginTop: '1vh' }}>
                            {compulsoryPois.map((item, index) => (
                            <ListItem key={index}>
                                <ListItemText primary={item} primaryTypographyProps={{ variant: "body1" }} />
                                <ListItemSecondaryAction>
                                <IconButton edge="end" onClick={() => handleDelete(index)}>
                                    <DeleteIcon />
                                </IconButton>
                                </ListItemSecondaryAction>
                            </ListItem>
                            ))}
                        </List>
                    </div>
                    </Paper>
                    <Grid container justifyContent="center" alignItems="center">
                        <Button
                        variant="contained"
                        color="primary"
                        size="large"
                        sx={{
                            top: '1vh',
                            backgroundColor: '#3B3A4C',
                            '&:hover': {
                            backgroundColor: '#5E5F71', // Button color on hover
                            },
                            fontSize: '1.5vh',
                            
                        }}
                        onClick={handleOnClick}
                        >
                        Create Route
                        </Button>
                    </Grid>
            </Grid>

        </div>
    )

}

export default PriorityPlaces