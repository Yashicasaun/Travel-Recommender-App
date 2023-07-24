import React, { useEffect, useRef, useState } from "react";
import {
  MapContainer,
  TileLayer,
  Marker,
  Popup,
  Polyline,
} from "react-leaflet";
import styles from "./InterestsScreen.module.css";
import "leaflet/dist/leaflet.css";
import L from "leaflet";
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import { ChevronLeft, ChevronRight } from "@mui/icons-material";
import { Icon } from "leaflet";
import { Select, MenuItem, Typography } from "@mui/material";
import fetchRoutes from "../../api/endpoints/route";
import { useLocation } from "react-router-dom";

function CreateRoute() {
  // const routes = {
  //   "Iterated Local Search":{'Day 1': [{'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'Start Point'}, {'name': 'Isarufer an der Reichenbachbrücke', 'value': [48.126804, 11.576537], 'subcategory': 'Beach'}, {'name': 'Nymphenburger Kanal', 'value': [48.158724, 11.51708], 'subcategory': 'Canal'}, {'name': 'Nymphenburg Palace (Schloss Nymphenburg)', 'value': [48.158311, 11.503469], 'subcategory': 'Museum'}, {'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'End Point'}], 'Day 2': [{'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'Start Point'}, {'name': 'New Town Hall (Neues Rathaus)', 'value': [48.137582, 11.575793], 'subcategory': 'Monument'}, {'name': 'Marienplatz', 'value': [48.137262, 11.575096], 'subcategory': 'Plaza'}, {'name': 'Rindermarkt', 'value': [48.13617, 11.574083], 'subcategory': 'Plaza'}, {'name': "St. Michael's Church (St. Michael)", 'value': [48.138546, 11.570284], 'subcategory': 'Structure'}, {'name': 'Luitpoldpark', 'value': [48.172595, 11.57036], 'subcategory': 'Park'}, {'name': 'Max-Joseph-Platz', 'value': [48.139852, 11.578247], 'subcategory': 'Theater'}, {'name': 'Antiquarium', 'value': [48.140547, 11.578958], 'subcategory': 'Historic and Protected Site'}, {'name': 'Dianatempel', 'value': [48.142975, 11.579994], 'subcategory': 'Monument'}, {'name': 'Hofgarten', 'value': [48.142925, 11.580047], 'subcategory': 'Urban Park'}, {'name': 'Bayerische Staatskanzlei', 'value': [48.142277, 11.58272], 'subcategory': 'Monument'}, {'name': 'House of Art (Haus der Kunst)', 'value': [48.144068, 11.585896], 'subcategory': 'Museum'}, {'name': 'Eisbach Wave (Eisbachwelle)', 'value': [48.143474, 11.587886], 'subcategory': 'Surf Spot'}, {'name': 'Englischer Garten', 'value': [48.151673, 11.592511], 'subcategory': 'Garden'}, {'name': 'Siegestor', 'value': [48.152338, 11.582115], 'subcategory': 'Landmarks and Outdoors'}, {'name': 'Dem Bayerischen Heere', 'value': [48.152417, 11.582035], 'subcategory': 'Historic and Protected Site'}, {'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'End Point'}], 'Day 3': [{'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'Start Point'}, {'name': 'Olympic Park (Olympiapark)', 'value': [48.173886, 11.54555], 'subcategory': 'Stadium'}, {'name': 'Olympiahalle', 'value': [48.174927, 11.550053], 'subcategory': 'Concert Hall'}, {'name': 'Olympiaberg', 'value': [48.16976, 11.551545], 'subcategory': 'Landmarks and Outdoors'}, {'name': 'Olympiapark SoccaFive Arena', 'value': [48.17497, 11.55615], 'subcategory': 'Stadium'}, {'name': 'Olympia-Eisstadion', 'value': [48.175093, 11.557058], 'subcategory': 'Stadium'}, {'name': 'BMW Museum', 'value': [48.176781, 11.558889], 'subcategory': 'Museum'}, {'name': 'Nationaltheater', 'value': [48.139566, 11.579386], 'subcategory': 'Music Venue'}, {'name': 'Bayerische Staatsoper', 'value': [48.139615, 11.579334], 'subcategory': 'Opera House'}, {'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'End Point'}]},
  //   "Ant Colony Optimization": {'Day 1': [{'name': 'Holiday Inn Express and Suites', 'value': [12.979867, 77.578864], 'subcategory': 'Start Point'}, {'name': 'Bull Temple', 'value': [12.965914, 77.657413], 'subcategory': 'Temple'}, {'name': 'Chinnaswamy Stadium', 'value': [12.978861, 77.599418], 'subcategory': 'Stadium'}, {'name': 'KSCA Club House', 'value': [12.977986, 77.600042], 'subcategory': 'Arts and Entertainment'}, {'name': 'Cubbon Park', 'value': [12.977173, 77.595288], 'subcategory': 'Park'}, {'name': "Tippu's Summer Palace", 'value': [12.959469, 77.57366], 'subcategory': 'Park'}, {'name': 'Bangalore Palace', 'value': [12.998409, 77.591948], 'subcategory': 'Monument'}, {'name': 'Freedom Park', 'value': [12.978176, 77.58236], 'subcategory': 'Park'}, {'name': 'Chitra Kala Parishad', 'value': [12.989239, 77.581011], 'subcategory': 'Art Gallery'}, {'name': 'Holiday Inn Express and Suites', 'value': [12.979867, 77.578864], 'subcategory': 'End Point'}]},
  //    "Greedy Randomized Adaptive Search Procedures" : {'Day 1': [{'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'Start Point'}, {'name': 'Denkmal-fuer-Michael-Jackson', 'value': [48.140281, 11.573416], 'subcategory': 'Monument'}, {'name': 'Englischer Garten', 'value': [48.151673, 11.592511], 'subcategory': 'Garden'}, {'name': 'Monopteros', 'value': [48.149863, 11.590922], 'subcategory': 'Monument'}, {'name': 'Siegestor', 'value': [48.152338, 11.582115], 'subcategory': 'Landmarks and Outdoors'}, {'name': 'Dem Bayerischen Heere', 'value': [48.152417, 11.582035], 'subcategory': 'Historic and Protected Site'}, {'name': 'Königsplatz', 'value': [48.145951, 11.56525], 'subcategory': 'Plaza'}, {'name': 'Städtische Galerie im Lenbachhaus', 'value': [48.14676, 11.563966], 'subcategory': 'Museum'}, {'name': 'Paläontologisches Museum', 'value': [48.147529, 11.563557], 'subcategory': 'History Museum'}, {'name': 'Alte Pinakothek', 'value': [48.148327, 11.569776], 'subcategory': 'Museum'}, {'name': 'Glyptothek', 'value': [48.146532, 11.565791], 'subcategory': 'History Museum'}, {'name': 'Architekturmuseum der TU München', 'value': [48.14702, 11.572219], 'subcategory': 'Art Museum'}, {'name': 'Museum Brandhorst', 'value': [48.148144, 11.574342], 'subcategory': 'Art Museum'}, {'name': 'NS-Dokumentationszentrum', 'value': [48.145429, 11.567476], 'subcategory': 'History Museum'}, {'name': 'Alter Botanischer Garten', 'value': [48.14238, 11.56461], 'subcategory': 'Park'}, {'name': 'Karlsplatz', 'value': [48.139069, 11.565978], 'subcategory': 'Plaza'}, {'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'End Point'}], 'Day 2': [{'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'Start Point'}, {'name': 'Marienplatz', 'value': [48.137262, 11.575096], 'subcategory': 'Plaza'}, {'name': 'Olympic Park (Olympiapark)', 'value': [48.173886, 11.54555], 'subcategory': 'Stadium'}, {'name': 'Olympiaberg', 'value': [48.16976, 11.551545], 'subcategory': 'Landmarks and Outdoors'}, {'name': 'BMW Museum', 'value': [48.176781, 11.558889], 'subcategory': 'Museum'}, {'name': 'Olympiapark SoccaFive Arena', 'value': [48.17497, 11.55615], 'subcategory': 'Stadium'}, {'name': 'SEA LIFE München', 'value': [48.173824, 11.556359], 'subcategory': 'Aquarium'}, {'name': 'House of Art (Haus der Kunst)', 'value': [48.144068, 11.585896], 'subcategory': 'Museum'}, {'name': 'Hofgarten', 'value': [48.142925, 11.580047], 'subcategory': 'Urban Park'}, {'name': 'Bayerische Staatskanzlei', 'value': [48.142277, 11.58272], 'subcategory': 'Monument'}, {'name': 'Nationaltheater', 'value': [48.139566, 11.579386], 'subcategory': 'Music Venue'}, {'name': 'Bayerische Staatsoper', 'value': [48.139615, 11.579334], 'subcategory': 'Opera House'}, {'name': 'Max-Joseph-Platz', 'value': [48.139852, 11.578247], 'subcategory': 'Theater'}, {'name': 'Feldherrnhalle', 'value': [48.141743, 11.577155], 'subcategory': 'Monument'}, {'name': 'Antiquarium', 'value': [48.140547, 11.578958], 'subcategory': 'Historic and Protected Site'}, {'name': 'Eisbach Wave (Eisbachwelle)', 'value': [48.143474, 11.587886], 'subcategory': 'Surf Spot'}, {'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'End Point'}], 'Day 3': [{'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'Start Point'}, {'name': 'Rindermarkt', 'value': [48.13617, 11.574083], 'subcategory': 'Plaza'}, {'name': 'Marstallmuseum', 'value': [48.15608, 11.50566], 'subcategory': 'History Museum'}, {'name': 'Nymphenburg Palace (Schloss Nymphenburg)', 'value': [48.158311, 11.503469], 'subcategory': 'Museum'}, {'name': 'Botanischer Garten München-Nymphenburg (Botanischer Garten)', 'value': [48.162651, 11.500261], 'subcategory': 'Garden'}, {'name': 'Gewächshäuser', 'value': [48.163716, 11.501614], 'subcategory': 'Garden'}, {'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'End Point'}]},
  //   "Simulated Annealing and Iterated Local Search": {'Day 1': [{'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'Start Point'}, {'name': 'Nationaltheater', 'value': [48.139566, 11.579386], 'subcategory': 'Music Venue'}, {'name': 'Marienplatz', 'value': [48.137262, 11.575096], 'subcategory': 'Plaza'}, {'name': 'Nymphenburg Palace (Schloss Nymphenburg)', 'value': [48.158311, 11.503469], 'subcategory': 'Museum'}, {'name': 'Ehrenhof', 'value': [48.158272, 11.504344], 'subcategory': 'Garden'}, {'name': 'Nymphenburger Kanal', 'value': [48.158724, 11.51708], 'subcategory': 'Canal'}, {'name': 'Isarufer an der Reichenbachbrücke', 'value': [48.126804, 11.576537], 'subcategory': 'Beach'}, {'name': 'Reichenbachbrücke', 'value': [48.127371, 11.576969], 'subcategory': 'Bridge'}, {'name': 'Corneliusbrücke', 'value': [48.128364, 11.580169], 'subcategory': 'Bridge'}, {'name': 'Deutsches Museum', 'value': [48.129902, 11.583512], 'subcategory': 'Museum'}, {'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'End Point'}], 'Day 2': [{'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'Start Point'}, {'name': 'Eisbach Wave (Eisbachwelle)', 'value': [48.143474, 11.587886], 'subcategory': 'Surf Spot'}, {'name': 'Englischer Garten', 'value': [48.151673, 11.592511], 'subcategory': 'Garden'}, {'name': 'Monopteros', 'value': [48.149863, 11.590922], 'subcategory': 'Monument'}, {'name': 'Siegestor', 'value': [48.152338, 11.582115], 'subcategory': 'Landmarks and Outdoors'}, {'name': 'Dem Bayerischen Heere', 'value': [48.152417, 11.582035], 'subcategory': 'Historic and Protected Site'}, {'name': 'Hofgarten', 'value': [48.142925, 11.580047], 'subcategory': 'Urban Park'}, {'name': 'Dianatempel', 'value': [48.142975, 11.579994], 'subcategory': 'Monument'}, {'name': 'Antiquarium', 'value': [48.140547, 11.578958], 'subcategory': 'Historic and Protected Site'}, {'name': 'Max-Joseph-Platz', 'value': [48.139852, 11.578247], 'subcategory': 'Theater'}, {'name': 'Bayerische Staatsoper', 'value': [48.139615, 11.579334], 'subcategory': 'Opera House'}, {'name': 'Kunsthalle München', 'value': [48.140042, 11.575858], 'subcategory': 'Art Museum'}, {'name': 'Denkmal-fuer-Michael-Jackson', 'value': [48.140281, 11.573416], 'subcategory': 'Monument'}, {'name': "St. Michael's Church (St. Michael)", 'value': [48.138546, 11.570284], 'subcategory': 'Structure'}, {'name': 'Deutsches Jagd- und Fischereimuseum', 'value': [48.138359, 11.571318], 'subcategory': 'Museum'}, {'name': 'Galerie Hegemann', 'value': [48.135924, 11.570186], 'subcategory': 'Art Gallery'}, {'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'End Point'}], 'Day 3': [{'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'Start Point'}, {'name': 'Rindermarkt', 'value': [48.13617, 11.574083], 'subcategory': 'Plaza'}, {'name': 'Olympic Park (Olympiapark)', 'value': [48.173886, 11.54555], 'subcategory': 'Stadium'}, {'name': 'Olympiaberg', 'value': [48.16976, 11.551545], 'subcategory': 'Landmarks and Outdoors'}, {'name': 'BMW Museum', 'value': [48.176781, 11.558889], 'subcategory': 'Museum'}, {'name': 'Olympia-Eisstadion', 'value': [48.175093, 11.557058], 'subcategory': 'Stadium'}, {'name': 'Olympiapark SoccaFive Arena', 'value': [48.17497, 11.55615], 'subcategory': 'Stadium'}, {'name': 'Olympiahalle', 'value': [48.174927, 11.550053], 'subcategory': 'Concert Hall'}, {'name': 'Luitpoldpark', 'value': [48.172595, 11.57036], 'subcategory': 'Park'}, {'name': 'Louis Hotel', 'value': [48.135871, 11.575756], 'subcategory': 'End Point'}]}
  // };
  // const distance = {
  //   "Iterated Local Search":{'Day 1': 13.6, 'Day 2': 12.98, 'Day 3': 11.6},
  //   "Ant Colony Optimization" : {'Day 1': 28.35,},
  //   "Greedy Randomized Adaptive Search Procedures" :{'Day 1': 8.72, 'Day 2': 14.30, 'Day 3': 12.97},
  //   "Simulated Annealing and Iterated Local Search": {'Day 1': 14.89, 'Day 2': 6.22, 'Day 3': 12.80}
  // };

  // const [selectedAlgorithm, setSelectedAlgorithm] = useState(
  //   Object.keys(routes)[0]
  // );
  const [routes, setRoutes] = useState({})
  const [distance,setDistance] = useState([])
  const [selectedAlgorithm, setSelectedAlgorithm] = useState("");
  const location = useLocation()
  const queryParams = new URLSearchParams(location.search);
  const [selectedDayIndex, setSelectedDayIndex] = useState("");
  const reactSlider = useRef()

  useEffect(() => {
    fetchRoutes(queryParams)
      .then((data) => {
        const {routes, distance} = data
        setRoutes(routes);
        setDistance(distance)
        console.log(routes)
        console.log(distance)
        setSelectedAlgorithm(Object.keys(routes)[0])
        setSelectedDayIndex("Day 1")
      }).then()
      .catch((error) => {
        console.error(error);
      });
  }, [])

  const handleAlgorithmChange = (event) => {
    setSelectedAlgorithm(event.target.value);
    setSelectedDayIndex("Day 1");
    reactSlider.current.slickGoTo(0);
  };

  const circleIcon = new Icon({
    iconUrl: require("./circle.svg").default,
    iconSize: [12, 12],
    iconAnchor: [6, 6],
  });

  const handleSliderChange = (index) => {
    setSelectedDayIndex(Object.keys(routes[selectedAlgorithm])[index]);
  };


  const sliderSettings = {
    dots: true,
    infinite: true,
    slidesToShow: 1,
    slidesToScroll: 1,
    speed: 500,
    prevArrow: <CustomPrevArrow />,
    nextArrow: <CustomNextArrow />,
    afterChange: handleSliderChange,
  };
  function CustomPrevArrow(props) {
    const { onClick } = props;

    return (
      <div className={styles.customPrevArrow} onClick={onClick}>
        <div className={styles.arrowCircle}>
          <ChevronLeft className={styles.arrowIcon} />
        </div>
        <span className="chevron-text" style={{position:'relative', left: '-1vw' ,marginTop: '1vh', fontSize:'1.5vh', fontWeight:'bold'}}>Previous Day</span>
      </div>
    );
  }

  function CustomNextArrow(props) {
    const { onClick } = props;
    return (
      <div className={styles.customNextArrow} onClick={onClick}>
        <div className={styles.arrowCircle}>
          <ChevronRight className={styles.arrowIcon} />
        </div>
        <span className="chevron-text" style={{position:'relative', right: '0vw', marginTop: '1vh', fontSize:'1.5vh', fontWeight:'bold'}}>Next Day</span>
      </div>
    );
  }

  const defaultCenter = [48.1351, 11.582];
  const defaultZoom = 14;

  //const colors = ["red", "blue", "black"]; // Array of colors for paths

  return (
    <div className={styles.InterestsScreen}>
      {Object.entries(routes).length > 0 ? (
        <div
          style={{
            //
            marginBottom: "2vh",
            marginLeft: "5vw",
            height: "70vh",
            width: "60vw",
          }}
        >
          <Select
            value={selectedAlgorithm}
            onChange={handleAlgorithmChange}
            style={{
              fontSize: "2vh",
              marginBottom: "2vh",
              minWidth: "0px",
              marginTop: "10vh",
            }}
          >
            {Object.entries(routes).map(
              ([algorithmName, algorithmData], algorithmIndex) => (
                <MenuItem key={algorithmName} value={algorithmName}>
                  <Typography variant="body1">{algorithmName}</Typography>
                </MenuItem>
              )
            )}
          </Select>
          <div
            className="map-container-div"
            style={{
              display: "flex",
              justifyContent: "space-between",
              flexDirection: "row",
              width: "80vw",
            }}
          >
            <div
              style={{
                minWidth: "0px",
                marginRight: "3vw",
                flex: 2,
                overflow: "hidden",
              }}
            >
              <Slider {...sliderSettings} ref={reactSlider}>
                {Object.entries(routes[selectedAlgorithm]).map(
                  ([day, places]) => {
                    const coordinates = places.map((item) => item.value);
                    const bounds = coordinates.reduce(
                      (bounds, coordinate) => bounds.extend(coordinate),
                      L.latLngBounds(coordinates[0], coordinates[0]) // Initialize with first coordinate
                    );
                    const center = bounds.getCenter();
                    const zoom = calculateZoomLevel(bounds);

                    return (
                      <div key={day}>
                        <MapContainer
                          center={center}
                          zoom={zoom}
                          style={{ height: "70vh", width: "60vw" }}
                        >
                          <TileLayer
                            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                            opacity={0.7}
                          />
                          <Polyline
                            positions={coordinates}
                            color="#6E6D73"
                            weight={3}
                          />
                          {/* {places.map(({name,value}) => {console.log("name",name,value)})} */}
                          {places.map(({ name, value }) => (
                            <Marker
                              key={name}
                              position={value}
                              icon={circleIcon}
                            >
                              <Popup>{name}</Popup>
                            </Marker>
                          ))}
                        </MapContainer>
                      </div>
                    );
                  }
                )}
              </Slider>
            </div>
            <div
              style={{
                minWidth: "0px",
                display: "flex",
                flex: 1,
                overflow: "hidden",
                flexDirection: "column",
                justifyContent: "space-around",
                alignItems: "stretch",
                fontWeight: "bold",
              }}
            >
              {/* Content of the second div */}
              <h3>{selectedDayIndex}</h3>
              <h4>Distance travelled = {distance[selectedAlgorithm][selectedDayIndex]} km</h4>
              {routes[selectedAlgorithm][selectedDayIndex].map(
                ({ name, value, subcategory }, index) => (
                  <div key={name}>
                    <body style={{ overflowWrap: "break-word" }}>
                      {index + 1}. {name} [{subcategory}]
                    </body>
                  </div>
                )
              )}
            </div>
          </div>
        </div>
      ) : (
        <div
          style={{
            //
            position: "absolute",
            top: "50%",
            left: "40%",
            fontWeight: "bold",
            fontSize: "3vh",
          }}
        >
          Loading routes...
        </div>
      )}
    </div>
  );
}

function calculateZoomLevel(bounds) {
  const WORLD_DIM = { height: 256, width: 256 };
  const ZOOM_MAX = 16;

  const ne = bounds.getNorthEast();
  const sw = bounds.getSouthWest();

  const latFraction = (Math.abs(ne.lat - sw.lat) / 180) * WORLD_DIM.height;
  const lngFraction = (Math.abs(ne.lng - sw.lng) / 360) * WORLD_DIM.width;

  const latZoom = Math.ceil(Math.log2(WORLD_DIM.height / latFraction));
  const lngZoom = Math.ceil(Math.log2(WORLD_DIM.width / lngFraction));

  return Math.min(ZOOM_MAX, Math.min(latZoom, lngZoom));
}

export default CreateRoute;
