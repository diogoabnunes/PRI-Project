import {Navbar,Container, Form, Button, FormControl} from "react-bootstrap";

export function NavBar() {
  return(
    <Navbar bg="light" variant="light">
    <Container>
      <Navbar.Brand href="/">
        <img
          alt="F1_Logo"
          src="/f1logo_white.png"
          width="70"
          height="30"
          className="d-inline-block align-top"
        />{' '}
      Formula 1
      </Navbar.Brand>
      <Form className="d-flex">
        <FormControl
          type="search"
          placeholder="Search"
          className="me-2"
          aria-label="Search"
        />
        <Button variant="outline-danger">Search</Button>
      </Form>
    </Container>
  </Navbar>
  )
}