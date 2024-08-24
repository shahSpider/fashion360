Key Models

Customer

    Represents individuals or companies that the business interacts with.
    Fields: name, email, phone, address, company, website, industry, etc.

Contact

    Represents people related to a Customer, often individuals within a Customer's organization.
    Fields: first_name, last_name, email, phone, position, customer (ForeignKey to Customer), etc.

Lead

    Represents potential customers who have shown interest but are not yet customers.
    Fields: name, email, phone, source, status, assigned_to (ForeignKey to User), etc.

Opportunity

    Represents potential deals or sales opportunities with a Customer.
    Fields: name, customer, value, stage, expected_close_date, assigned_to, etc.

Activity (Task/Interaction)

    Tracks interactions, tasks, or follow-ups with a Customer or Lead.
    Fields: title, description, activity_type (call, meeting, email, etc.), date, status, related_to (GenericForeignKey to Customer/Lead), etc.

User

    Represents the system users, usually the sales team or customer service representatives.

    Extend Django’s default User model to include CRM-specific fields like role or assigned_customers.

Note

    Allows users to add notes related to a Customer, Lead, or Opportunity.
    Fields: content, created_by (ForeignKey to User), timestamp, related_to (GenericForeignKey), etc.