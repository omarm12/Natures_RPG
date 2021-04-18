import React from 'react'

function SortObs(props) {
    console.log(props)
    if (props.sort === "Reverse") {
        console.log("Yea")
        props.data.reverse()
        // props.items(props.data.reverse())
        console.log(props.data)
    }

    return (
        <div>
        </div>
    )
}

export default SortObs