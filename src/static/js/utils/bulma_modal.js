class BulmaModal {
    constructor(modalId, options = {}) {
        this.options = options;
        this.modal = document.getElementById(modalId);
        if (!this.modal) {
            throw new Error(`Modal with ID ${modalId} not found`);
        }

        this.#renderModal();

        this.deleteButton = this.modal.querySelector('.delete') || this.modal.querySelector(this.options.deleteButtonSelector);
        this.closeButton = this.modal.querySelector('.modal-close') || this.model.querySelector(this.options.closeButtonSelector);
        this.cancelButton = this.modal.querySelector('.cancel-button') || this.modal.querySelector(this.options.cancelButtonSelector);
        if (this.deleteButton) {
            this.deleteButton.addEventListener('click', () => this.close());
        }
        if (this.closeButton) {
            this.closeButton.addEventListener('click', () => this.close());
        }
        if (this.cancelButton) {
            this.cancelButton.addEventListener('click', () => this.close());
        }
    }

    open() {
        this.modal.classList.add('is-active');
    }

    close() {
        this.modal.classList.remove('is-active');
    }

    #renderModal() {
        if (Object.hasOwn(this.options, 'title') && this.options.title) {
            let modalCard = this.modal.querySelector('.modal-card');
            if (!modalCard) {
                modalCard = document.createElement('div');
                modalCard.className = 'modal-card';
                this.modal.appendChild(modalCard);
            }
            modalCard.innerHTML = '';

            let modalCardHead = this.modal.querySelector('.modal-card .modal-card-head');
            if (!modalCardHead) {
                modalCardHead = document.createElement('header');
                modalCardHead.className = 'modal-card-head';
                modalCard.appendChild(modalCardHead);
            }

            let titleElement = this.modal.querySelector('.modal-card .modal-card-head .modal-card-title');
            if (!titleElement) {
                titleElement = document.createElement('p');
                titleElement.className = 'modal-card-title';
                modalCardHead.appendChild(titleElement);
            }
            titleElement.textContent = this.options.title;

            let closeButton = this.modal.querySelector('.modal-card .modal-card-head .delete');
            if (!closeButton) {
                closeButton = document.createElement('button');
                closeButton.className = 'delete';
                closeButton.setAttribute('aria-label', 'close');
                modalCardHead.appendChild(closeButton);
            }
        }

        if (Object.hasOwn(this.options, 'contentHTML') && this.options.contentHTML) {
            let modalCard = this.modal.querySelector('.modal-card');
            if (!modalCard) {
                modalCard = document.createElement('div');
                modalCard.className = 'modal-card';
                this.modal.appendChild(modalCard);
            }

            let bodyElement = this.modal.querySelector('.modal-card .modal-card-body');
            if (!bodyElement) {
                bodyElement = document.createElement('section');
                bodyElement.className = 'modal-card-body';
                modalCard.appendChild(bodyElement);
            }
            bodyElement.innerHTML = this.options.contentHTML || '';

            const contentElement = this.modal.querySelector('.modal .modal-content');
            if (contentElement) {
                contentElement.remove();
            }
        }
    }
}