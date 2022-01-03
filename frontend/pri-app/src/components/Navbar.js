import {Navbar,Container, Form, Button, FormControl, Col} from "react-bootstrap";

export function NavBar() {
  return(
    <Navbar bg="dark" variant="dark">
    <Container fluid>
      <Navbar.Brand href="/">
        <img
          alt="F1_Logo"
          src="/f1logo_removedbg.png"
          width="70"
          height="30"
          className="d-inline-block align-top"
        />{' '}
      Formula 1
      </Navbar.Brand>
      <Form className="d-flex" >
          <FormControl
            className="w-50"
            type="search"
            placeholder="Search"
            className="me-2"
            aria-label="Search"
          />
        <Button variant="outline-light">Search</Button>
      </Form>
    </Container>
  </Navbar>
  )
}