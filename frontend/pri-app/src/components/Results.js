import {Card} from "react-bootstrap"

export function Results() {
    const items = [];
    items.push(card1());   
    items.push(card2());        
    items.push(card3());        
    items.push(card4());        
    items.push(card5());        

    return(
        <div>
            {items}
        </div>
    )
}

function card1(){
    return(
        <Card className="m-4">
            <Card.Header>Race: 2020 Portuguese Grand Prix</Card.Header>
            <Card.Body>
            <blockquote className="blockquote mb-0 d-flex">
                <p>
                {' '}
                The 2020 Portuguese Grand Prix (officially known as the Formula 1 Heineken Grande Prémio de Portugal 2020) was a Formula One motor race that was held on 25 October 2020 at the Algarve International Circuit in Portimão, Portugal.
                It was the first Portuguese Grand Prix held since 1996 and the first time held at the Algarve International Circuit.
                The race was the twelfth round of the 2020 Formula One World Championship.
                Hamilton's victory put him ahead of Michael Schumacher for most victories in Formula One with 92.{' '}
                <a href="/">See more</a></p>
            </blockquote>
            </Card.Body>
        </Card>
    )
}

function card2(){
    return(
        <Card className="m-4">
            <Card.Header>Driver: Lewis Hamilton</Card.Header>
            <Card.Body>
            <blockquote className="blockquote mb-0 d-flex">
                <p>
                {' '}
                Sir Lewis Carl Davidson Hamilton MBE HonFREng (born 7 January 1985) is a British racing driver.
                He currently competes in Formula One for Mercedes, having previously driven for McLaren from 2007 to 2012.
                In Formula One, Hamilton has won a joint-record seven World Drivers' Championship titles (tied with Michael Schumacher), and holds the records for the most wins (103), pole positions (103), and podium finishes (182), among others.{' '}
                <a href="/">See more</a></p>
            </blockquote>
            </Card.Body>
        </Card>
    )
}

function card3(){
    return(
        <Card className="m-4">
            <Card.Header>Constructor: Ferrari</Card.Header>
            <Card.Body>
            <blockquote className="blockquote mb-0 d-flex">
                <p>
                {' '}
                Scuderia Ferrari S.p.A. (Italian: [skudeˈriːa ferˈraːri]) is the racing division of luxury Italian auto manufacturer Ferrari and the racing team that competes in Formula One racing.
                The team is also nicknamed "The Prancing Horse", in reference to their logo.
                It is the oldest surviving and most successful Formula One team, having competed in every world championship since the 1950 Formula One season.{' '}
                <a href="/">See more</a></p>
            </blockquote>
            </Card.Body>
        </Card>
    )
}

function card4(){
    return(
        <Card className="m-4">
            <Card.Header>Circuit: Portimao</Card.Header>
            <Card.Body>
            <blockquote className="blockquote mb-0 d-flex">
                <p>
                {' '}
                The Algarve International Circuit (Portuguese: Autódromo Internacional do Algarve), commonly referred to as Portimão Circuit, is a 4.653 km (2.891 mi) race circuit located in Portimão, Algarve region, in Portugal.
                The development includes a karting track, off-road track, technology park, five-star hotel, sports complex and apartments.
                The circuit was designed by Ricardo Pina, Arquitectos.
                The Construction was finished in October 2008 and the circuit was homologated by both the FIM on 11 October 2008 and the FIA two days later. The total cost was €195 million (approximately $250 million).{' '}
                <a href="/">See more</a></p>
            </blockquote>
            </Card.Body>
        </Card>
    )
}

function card5(){
    return(
        <Card className="m-4">
            <Card.Header>Page: DHL Fastest Lap Award</Card.Header>
            <Card.Body>
            <blockquote className="blockquote mb-0 d-flex">
                <p>
                {' '}
                The DHL Fastest Lap Award is given annually by the courier, Formula One global partner and logistics provider DHL "to recognise the driver who most consistently demonstrates pure speed, with the fastest lap at the highest number of races each season", and to reward the winning driver for "characteristics such as excellent performance, passion, can-do attitude, reliability and precision".
                {' '}
                <a href="/">See more</a></p>
            </blockquote>
            </Card.Body>
        </Card>
    )
}