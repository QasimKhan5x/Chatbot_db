def get_fees_due(cms_id):
    '''make view of sums first'''
    pass

def get_fees_due_date(cms_id):
    return f'SELECT dueDate FROM feeInfo WHERE cms_id = "{cms_id}" AND paid = false;'

def is_fees_paid(cms_id):
    return f'SELECT * FROM feeInfo WHERE cms_id = "{cms_id}" AND paid = false;'