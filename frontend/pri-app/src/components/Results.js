import {Card} from "react-bootstrap"

export function Results() {
    const items = [];
    for(var i = 0; i < 5; i++) {
        items.push(card());        
    }
    return(
        <div>
            {items}
        </div>
    )
}

function card(){
    return(
        <Card className="m-4">
            <Card.Header>Race</Card.Header>
            <Card.Body>
            <blockquote className="blockquote mb-0">
                <p>
                {' '}
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere
                erat a ante.{' '}
                </p>
            </blockquote>
            </Card.Body>
        </Card>
    )
}