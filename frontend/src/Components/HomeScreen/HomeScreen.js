import styles from "./HomeScreen.module.css"
import Searchbar from "./Searchbar/Searchbar"
import Apptext from "./Apptext/Apptext"

function HomeScreen() {
    return (
        <div className = {styles.HomeScreen}>
            <Searchbar/>
            <Apptext/>
        </div>
    )
}

export default HomeScreen