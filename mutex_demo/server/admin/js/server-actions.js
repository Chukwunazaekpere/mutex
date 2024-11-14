import axios from axios


export async function getUserLogs() {
    try {
        const logs = await axios.get("/get-logs");
        console.log("\n\t Logs: ", logs)
    } catch (error) {
        
    }
}