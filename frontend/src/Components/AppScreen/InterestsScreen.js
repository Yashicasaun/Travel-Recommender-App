import styles from "./InterestsScreen.module.css";
import { Box, Typography, List, ListItem, Checkbox, Button, TextField } from "@mui/material";
import { useNavigate, useLocation } from "react-router-dom";
import { useEffect, useState } from "react";
import {fetchCategories, fetchSubcategories} from "../../api/endpoints/categories"

function InterestScreen() {
  
  const [categories, setCategories] = useState([])
  const [selectedCategories, setSelectedCategories] = useState([]);
  const [distance, setDistance] = useState()
  const [maxLocation, setMaxLocation] = useState()

  const location = useLocation();
  const navigate = useNavigate();
  const queryParams = new URLSearchParams(location.search);
  const city = queryParams.get('city')

  useEffect(() => {
    fetchCategories(city).then(
      data => {
        setCategories(data)
      }
    )
  }, [])

  const handleOnClick = () => {
    if (selectedCategories.length === 0) {
      alert("Please select at least one category");
    } 
    else if (distance === undefined) {
      alert("Please specify maximum distance");
    }
    else if (maxLocation === undefined) {
      alert("Please specify maximum number of locations");
    }
    else {
      queryParams.append("categories", selectedCategories);
      queryParams.append('max_distance', distance);
      queryParams.append('max_locations', maxLocation);
      navigate(`/prioritypois?${queryParams.toString()}`);
    }
  };

  const handleDistanceChange = (event) => {
    setDistance(event.target.value)
  }

  const handlemaxLocation = (event) => {
    setMaxLocation(event.target.value)
  }

  const handleCategoryChange = (event, value) => {
    if (event.target.checked) {
      setSelectedCategories((prevSelectedCategories) => [...prevSelectedCategories, value]);
    } else {
      setSelectedCategories((prevSelectedCategories) =>
        prevSelectedCategories.filter((category) => category !== value)
      );
      console.log(selectedCategories)
    }
  };

  return (
    <div className={styles.InterestsScreen} style={{textAlign : "left"}}>
            <Box
            position="fixed"
            //  top="12%"
            //  left="10%"
             marginLeft= '10%'
             paddingTop= '8%'
             width="80vw"
             height="100%"
             display="flex"
             justifyContent="left"
             alignItems="left"
             flexDirection="column"
             textAlign="left"
            >
                <Typography variant="h5"  gutterBottom>
                Choose your Interests
                </Typography>
                <List>
                {categories.map((category) => (
                    <ListItem key={category.label} sx={{ display: 'flex', alignItems: 'center' }} disablePadding>
                        <Checkbox
                        id={category.value}
                        onChange={(event) => handleCategoryChange(event, category.value)}
                        checked={selectedCategories.includes(category.value)}
                        />
                        <label htmlFor={category.value}>
                            <Typography variant="h6" component="span">
                            {category.label}
                            </Typography>
                        </label>
                    </ListItem>
                ))}
                </List>
                <br/>
                <div style={{display: "flex", flexDirection: "row"}}>
                  <Typography variant="h6">What is the maximum distance you are willing to travel per day?</Typography>
                  <TextField
                    label="distance( in kilometers )"
                    variant="outlined"
                    sx = {{
                      marginLeft: '1vw',
                      width: 'auto',
                    }}
                    onChange={handleDistanceChange}
                    value = {distance}
                  />
                </div>
                <br/>
                <div style={{display: "flex", flexDirection: "row"}}>
                  <Typography variant="h6">What is the maximum number of locations you are willing to travel per day?</Typography>
                  <TextField
                    label="Number of Locations"
                    variant="outlined"
                    sx = {{
                      marginLeft: '1vw',
                      width: 'auto',
                    }}
                    onChange={handlemaxLocation}
                    value = {maxLocation}
                  />
                </div>
                <br/>
                <Button variant="contained"  size="large" 
                    sx={{
                        backgroundColor:"#ECF1FB",
                        '&:hover': {
                        backgroundColor: '#C1CDE2', // Button color on hover
                        },
                        color: "black",
                        fontSize: '1.5vh',
                        width: "10%"}}
                        onClick={handleOnClick}>
                    Next
                </Button>
            </Box>
        </div>
  );
}

export default InterestScreen;
