```mermaid
erDiagram

accounts ||--o{ events: ""
accounts ||--o{ years: ""
years ||--o{ months: ""
months ||--o{ weeks: ""


accounts {
  string name
  string password
  string email
}

events {
  string title
  text detail
  date date
}

years {
  string title
  date start_time 
  integer span
}

months {
  string title
  date start_time 
  integer span
}

weeks {
  string title
  date start_timeS
  integer span
}

```