columns_to_drop = ['comments_to_the_relevant_team_lead', 'reviewed',
                   'team_lead_answer', 'update_id']

new_column_names = {'effort_in_q1' : 'Q1 Effort',
                'effort_in_q1_next_year' : '2020 Q1 Effort',
                'effort_in_q2' : 'Q2 Effort',
                'effort_in_q2_next_year' : '2020 Q2 Effort',
                'effort_in_q3' : 'Q3 Effort',
                'effort_in_q4' : 'Q4 Effort',
                'goal___timeframe' : 'Goal Timeframe',
                'goal___title' : 'Goal Title',
                'goal_owner' : 'Goal Owner',
                'it_team' : 'IT Team',
                'request' : 'Request',
                'response' : 'Response'}

new_columns_ordered = ['Goal Title', 'IT Team', 'Goal Owner', 'Goal Timeframe',
                       'Q1 Effort', 'Q2 Effort', 'Q3 Effort', 'Q4 Effort', '2020 Q1 Effort',
                       '2020 Q2 Effort', 'Request', 'Response']
