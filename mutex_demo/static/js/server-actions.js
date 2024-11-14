

async function getUserLogs() {
    try {
        const logs = await fetch("get-logs");
        console.log("\n\t logs: ", logs);
        if(logs.ok){
            const resp = await logs.d()
            console.log("\n\t Logs: ", resp);
            // return
        };
        throw new Error(logs.statusText)
    } catch (error) {
        console.log("\n\t error: ", error.message);
        
    }
}